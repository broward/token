// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract QuorumGenericContract {
    // State variables
    address public owner;
    string public contractName;
    uint256 public creationTime;

    struct DataEntry {
        uint256 id;
        string data;
        address sender;
        uint256 timestamp;
    }

    DataEntry[] public entries;
    mapping(uint256 => DataEntry) private entryById;
    uint256 public nextId;

    // Events
    event DataAdded(uint256 indexed id, string data, address indexed sender, uint256 timestamp);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Constructor
    constructor(string memory _contractName) {
        owner = msg.sender;
        contractName = _contractName;
        creationTime = block.timestamp;
    }

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier validData(string memory _data) {
        require(bytes(_data).length > 0, "Data cannot be empty");
        _;
    }

    // Functions

    // Add a new data entry
    function addData(string memory _data) public validData(_data) {
        uint256 currentId = nextId;
        entries.push(DataEntry(currentId, _data, msg.sender, block.timestamp));
        entryById[currentId] = DataEntry(currentId, _data, msg.sender, block.timestamp);
        nextId++;
        emit DataAdded(currentId, _data, msg.sender, block.timestamp);
    }

    // Retrieve a specific entry by ID
    function getDataById(uint256 _id) public view returns (DataEntry memory) {
        require(_id < nextId, "Invalid ID");
        return entryById[_id];
    }

    // Get the number of entries
    function getEntryCount() public view returns (uint256) {
        return entries.length;
    }

    // Transfer ownership
    function transferOwnership(address _newOwner) public onlyOwner {
        require(_newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }
}

