// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleBank {

    mapping (address => uint256) public balance;
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function deposit() public payable {
        balance[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) public {
        require(balance[msg.sender] >= amount, "Insufficient Balance!");
        balance[msg.sender] -= amount;
        (bool success,) = payable (msg.sender).call{value: amount}("");
        require(success, "Transfer Failed!");
    }

    function getMyBalance() public view returns (uint256) {
        return balance[msg.sender];
    }


}