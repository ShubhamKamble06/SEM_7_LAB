// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract MarksManagmtSys {
    // Structure
    struct Student {
        int256 ID;
        string fName;
        string lName;
        int256 marks;
    }

    address public owner;
    int256 public stdCount = 0;
    // Mapping
    mapping(int256 => Student) public stdRecords;

    modifier onlyOwner() {
        require(owner == msg.sender, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    // Create a function to add
    // the new records
    function addNewRecords(
        int256 _ID,
        string memory _fName,
        string memory _lName,
        int256 _marks
    ) public onlyOwner {
        // Increase the count by 1
        stdCount = stdCount + 1;

        // Fetch the student details
        // with the help of stdCount
        stdRecords[stdCount] = Student(_ID, _fName, _lName, _marks);
    }

    function getAllRecords() public view returns (Student[] memory) {
        Student[] memory records = new Student[](uint256(stdCount));

        for (int256 i = 1; i <= stdCount; i++) {
            records[uint256(i - 1)] = stdRecords[i];
        }

        return records;
    }

     fallback() external {
        revert("Fallback function called. Function not found.");
    }
}
