
pragma solidity >=0.8.2 <0.9.0; // similar to C and C++, pragma is a directive that specifies the compiler version 

// This is a single-line comment
/**
 * This is multi-line comments
 */


// This is a contract called Storage. A contract is similar to a class in OOP languages and each instance of a contract 
// needs to be deployed in the blockchain (i.e. each one of them has its own address, Ethereum calls these "autonomous agents")
contract Storage {

    uint256 number; // This is a state variable (i.e. a value that defines the state of the contract). 
		 /**
     * There are 3 scopes for state variables. Either it is 1. public (i.e. other contracts can access it)
		 * 2. internal => default (i.e. similar to protected in Java, only this contract or derived contract can access it)
		 * 3. private (i.e. only the current contract can access it).
     */

    /**
     * This is a method definition. In this case, this is a method called store that takes in 1 parameter of num that is an 
		 * unsigned integer of 256 bits long (i.e 32 bytes long), and has an access modifier called public which follows same semantic as 
		 * the state variable scoping.  
     */
    function store(uint256 num) public {
        number = num; // assign the parameter into the state variable
    }

    /**
     * a read-only method that returns 1 result (like Python, it can return a tuple of results) of type uint256 
     * view means it is a read-only method that doesn't alter the state variable. 
     */
    function retrieve() public view returns (uint256){
        return number;
    }
}