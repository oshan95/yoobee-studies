// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    struct Vote {
        address receiver;
        uint256 timestamp;
    }

    mapping (address => Vote) public votes;
    bool public voting;

    event AddVote (address indexed voter, address indexed reciever, uint256 timestamp);
    event RemoveVote (address indexed voter);
    event StartVoting (address indexed startedBy);
    event StopVoting (address indexed stoppedBy);

    constructor() {
        voting = false;
    }

    function startVote() external returns (bool) {
        voting = true;
        emit StartVoting(msg.sender);
        return true;
    }

    function stopVote() external returns (bool) {
        voting = false;
        emit StopVoting(msg.sender);
        return true;
    }

    function removeVote() external returns (bool) {
        require (voting, "Voting is not active.");
        delete votes[msg.sender];
        emit RemoveVote(msg.sender);
        return true;
    }

    function addVote(address reciever) external returns (bool) {
        require (voting, "Voting is active.");
        votes[msg.sender] = Vote(reciever, block.timestamp);
        emit AddVote(msg.sender, reciever, block.timestamp);
        return true;
    }

    function getVote(address voterAddress) external view returns (address candidateAddress) {
        return votes[voterAddress].receiver;
    }

}