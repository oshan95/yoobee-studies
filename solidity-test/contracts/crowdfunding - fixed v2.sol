// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

/**
 * @title CrowdFunding
 * @dev Decentralized crowdfunding contract with proposal voting and refund mechanism.
 *
 * Fixes applied:
 *  1. Implemented all empty function bodies (contribute, refund, createRequest, voteRequest, makePayment)
 *  2. Fixed broken createRequest() function signature
 *  3. Added reentrancy guard (ReentrancyGuard) to refund() and makePayment()
 *  4. Added double-vote prevention in voteRequest()
 *  5. Raised minimumContribution from 100 wei to 0.01 ETH
 *  6. Fixed refund() logic — should only work AFTER deadline, not before
 *  7. Added events for all key state changes
 *  8. Added nonReentrant modifier pattern to prevent reentrancy attacks
 */
contract CrowdFunding {

    // ─── State Variables ───────────────────────────────────────────────────────

    address public owner;
    uint256 public minimumContribution;
    uint256 public deadline;
    uint256 public target;
    uint256 public raisedAmount;
    uint256 public totalContributors;
    uint256 public numRequests;

    // FIX 8: Simple reentrancy guard
    bool private _locked;

    // ─── Structs ────────────────────────────────────────────────────────────────

    struct Request {
        string description;
        address payable recipient;
        uint256 value;
        bool completed;
        uint256 noOfVoters;
        mapping(address => bool) voters;
    }

    // ─── Mappings ───────────────────────────────────────────────────────────────

    mapping(uint256 => Request) public allRequests;
    mapping(address => uint256) public contributors;

    // ─── Events ─────────────────────────────────────────────────────────────────

    // FIX 7: Events added for all key actions
    event ContributionReceived(address indexed contributor, uint256 amount);
    event RefundIssued(address indexed contributor, uint256 amount);
    event RequestCreated(uint256 indexed requestId, string description, address recipient, uint256 value);
    event VoteCast(uint256 indexed requestId, address indexed voter);
    event PaymentMade(uint256 indexed requestId, address indexed recipient, uint256 value);

    // ─── Constructor ────────────────────────────────────────────────────────────

    constructor(uint256 _target, uint256 _deadline) {
        owner = msg.sender;
        deadline = block.timestamp + _deadline;
        target = _target;
        // FIX 5: Raised minimum from 100 wei to 0.01 ETH to prevent trivial voting rights
        minimumContribution = 0.01 ether;
    }

    // ─── Modifiers ──────────────────────────────────────────────────────────────

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can access this function.");
        _;
    }

    modifier deadlineNotPassed() {
        require(
            block.timestamp < deadline,
            "Crowdfunding deadline has passed."
        );
        _;
    }

    modifier deadlinePassed() {
        // FIX 6: refund() should only be callable AFTER deadline
        require(
            block.timestamp >= deadline,
            "Deadline has not passed yet."
        );
        _;
    }

    modifier isContributor() {
        require(
            contributors[msg.sender] > 0,
            "You are not a contributor."
        );
        _;
    }

    // FIX 8: Reentrancy guard modifier
    modifier nonReentrant() {
        require(!_locked, "Reentrant call detected.");
        _locked = true;
        _;
        _locked = false;
    }

    // ─── Functions ──────────────────────────────────────────────────────────────

    /// @notice Returns the current ETH balance held by the contract
    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }

    /// @notice Contribute ETH to the crowdfunding campaign
    // FIX 1: Implemented contribute() body
    function contribute() public payable deadlineNotPassed {
        require(
            msg.value >= minimumContribution,
            "Contribution is below the minimum required amount."
        );

        // First-time contributor: increment count
        if (contributors[msg.sender] == 0) {
            totalContributors++;
        }

        contributors[msg.sender] += msg.value;
        raisedAmount += msg.value;

        emit ContributionReceived(msg.sender, msg.value);
    }

    /// @notice Refund contributor if target was not met after deadline
    // FIX 1: Implemented refund() body
    // FIX 3 & 8: Added nonReentrant guard
    // FIX 6: Uses deadlinePassed modifier (was incorrectly using isDeadlinePassed which blocked after deadline)
    function refund() public deadlinePassed isContributor nonReentrant {
        require(
            raisedAmount < target,
            "Target was reached: refunds are not available."
        );

        uint256 amount = contributors[msg.sender];
        require(amount > 0, "No funds to refund.");

        // Zero out before transfer to prevent reentrancy
        contributors[msg.sender] = 0;
        raisedAmount -= amount;
        totalContributors--;

        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "Refund transfer failed.");

        emit RefundIssued(msg.sender, amount);
    }

    /// @notice Owner creates a spending proposal for contributors to vote on
    // FIX 1 & 2: Fixed broken function signature and implemented body
    function createRequest(
        string memory _description,
        address payable _recipient,
        uint256 _value
    ) public onlyOwner {
        require(
            _value <= address(this).balance,
            "Requested value exceeds contract balance."
        );
        require(_recipient != address(0), "Invalid recipient address.");

        Request storage newRequest = allRequests[numRequests];
        newRequest.description = _description;
        newRequest.recipient = _recipient;
        newRequest.value = _value;
        newRequest.completed = false;
        newRequest.noOfVoters = 0;

        emit RequestCreated(numRequests, _description, _recipient, _value);

        numRequests++;
    }

    /// @notice Vote for a spending proposal (one vote per contributor)
    // FIX 1: Implemented voteRequest() body
    // FIX 4: Added double-vote prevention
    function voteRequest(uint256 _requestNo) public isContributor {
        require(_requestNo < numRequests, "Request does not exist.");

        Request storage request = allRequests[_requestNo];

        require(!request.completed, "This request has already been completed.");
        // FIX 4: Prevent double voting
        require(
            !request.voters[msg.sender],
            "You have already voted for this request."
        );

        request.voters[msg.sender] = true;
        request.noOfVoters++;

        emit VoteCast(_requestNo, msg.sender);
    }

    /// @notice Execute payment for a proposal if majority voted yes
    // FIX 1: Implemented makePayment() body
    // FIX 3 & 8: Added nonReentrant guard
    function makePayment(uint256 _requestNo) public onlyOwner nonReentrant {
        require(_requestNo < numRequests, "Request does not exist.");
        require(raisedAmount >= target, "Funding target has not been reached.");

        Request storage request = allRequests[_requestNo];

        require(!request.completed, "Payment already made for this request.");
        require(
            request.noOfVoters > totalContributors / 2,
            "Majority vote not reached: need more than 50% of contributors."
        );
        require(
            request.value <= address(this).balance,
            "Insufficient contract balance."
        );

        request.completed = true;

        (bool success, ) = request.recipient.call{value: request.value}("");
        require(success, "Payment transfer failed.");

        emit PaymentMade(_requestNo, request.recipient, request.value);
    }
}
