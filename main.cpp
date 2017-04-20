#include <iostream>

using namespace std;

/* -------------------------------------------------------------------------------------
 * LINKED LIST CLASS
 *   Manages nodes
 *   Contains the start of the node list
 * ---------------------------------------------------------------------------------- */
class lList{
public:
    lList();
    lList(Node * startPoint);
    bool addElement(Node * newNode);
    bool delElement(string PassengerName);
    bool searchElement(string PassengerName);
    void printAll();
private:
    int listLength;
    Node * listStart;
};

lList::lList(){
    listStart = NULL;
    listLength = 0;
}

lList::lList(Node * startPoint){
    listStart = startPoint;
    listLength = 1;
}

bool lList::addElement(Node * newNode) {
    if(listLength == 0){
        listStart = newNode;
        listLength ++;
        return true;
    }
    else if(listLength > 0){
        Node * currentNode = listStart;
        while (currentNode->getNext() != NULL){
            currentNode = currentNode->getNext();
        }
        currentNode->setNext(newNode);
        listLength ++;
        return true;
    }
    return false;
}

bool lList::delElement(string PassengerName) {
    Node * currentNode = listStart;
    while (currentNode != NULL){
        if(currentNode->getValue()->getPassengerName() == PassengerName){
            Node * previousNode = currentNode->getPrevious();
            Node * nextNode = currentNode->getNext();
            nextNode->setPrevious(previousNode);
            previousNode->setNext(nextNode);
            delete(currentNode);
            return true;
        }
        else{
            currentNode = currentNode->getNext();
        }
    }
    return false;
}

bool lList::searchElement(string PassengerName) {
    Node * currentNode = listStart;
    while (currentNode->getValue()->getPassengerName() != PassengerName && currentNode != NULL){
        currentNode = currentNode->getNext();
    }
    return currentNode != NULL;
}

void lList::printAll() {
    Node * currentNode = listStart;
    while (currentNode != NULL){
        cout << "\nPassenger Name: " << currentNode->getValue()->getPassengerName() << endl;
        cout << "Ticket Number: " << currentNode->getValue()->getTicketNumber() << endl;
        currentNode = currentNode->getNext();
    }
}

/* -------------------------------------------------------------------------------------
 * NODE
 *   Contains the next node and previous node addresses and Ticket information
 * ---------------------------------------------------------------------------------- */
class Node{
public:
    Node();
    Node(Ticket * store);
    Node * getNext();
    Node * getPrevious();
    Ticket * getValue();
    bool setNext(Node * newNext);
    bool setPrevious(Node * newPrevious);
private:
    Ticket * value;
    Node * lastNode;
    Node * nextNode;
};

Node::Node(){
    value = NULL;
    lastNode = NULL;
    nextNode = NULL;
}
Node::Node(Ticket * store){
    value = store;
    lastNode = NULL;
    nextNode = NULL;
}
Node * Node::getNext() {
    return nextNode;
}
bool Node::setNext(Node * newNext) {
    nextNode = newNext;
    return true;
}
Node * Node::getPrevious() {
    return lastNode;
}
bool Node::setPrevious(Node * newPrevious) {
    lastNode = newPrevious;
    return true;
}

Ticket *Node::getValue() {
    return value;
}

/* -------------------------------------------------------------------------------------
 * TICKET
 *   Contains information for the passenger.
 *   Data section of the linked list
 * ---------------------------------------------------------------------------------- */
class Ticket{
public:
    Ticket(string name);
    string getPassengerName();
    long getTicketNumber();
private:
    string passengerName;
    long ticketNumber;
};

Ticket::Ticket(string name) {
    passengerName = name;
}

long Ticket::getTicketNumber() {
    return ticketNumber;
}

string Ticket::getPassengerName() {
    return passengerName;
}

/* -------------------------------------------------------------------------------------
 * FLIGHT
 *   Contains the instance of the list of node tickets
 *   performs operations in editing the list of tickets
 * ---------------------------------------------------------------------------------- */
class Flight{
public:
    Flight(string flightID);
    bool newTicket();
    bool delTicket();
    bool checkTicket();
    void printManifest();
    //string getFlightNumber();
private:
    static string flightNumber;
    lList manifest;
};

Flight::Flight(string flightID){
    flightNumber = flightID;
    manifest = lList();
}

bool Flight::newTicket() {
    string passName;
    cout << "Name of the new Passenger: ";
    cin >> passName;
    Ticket newPassenger = Ticket(passName);
    Node newNode = Node(&newPassenger);
    return manifest.addElement(&newNode);
}

bool Flight::delTicket() {
    string passName;
    cout << "Enter the name of the passenger to remove: ";
    cin >> passName;
    return manifest.delElement(passName);
}

bool Flight::checkTicket(){
    string passName;
    cout << "Enter the name of the passenger to verify: ";
    cin >> passName;
    return manifest.searchElement(passName);
}

void Flight::printManifest(){
    cout << "Printing the flight manifest for Flight number " << flightNumber << endl;
    manifest.printAll();
}

//string Flight::getFlightNumber() {
//    return flightNumber;
//}
/* -------------------------------------------------------------------------------------
 * MAIN
 * ---------------------------------------------------------------------------------- */
int main() {
    int selection;
    Flight mainFlight = Flight("DL7982");
    do {
        cout << "Airline Ticket Reservation Program" << endl;
        cout << "  1 - New Reservation" << endl;
        cout << "  2 - Cancel Reservation" << endl;
        cout << "  3 - Check Reservation" << endl;
        cout << "  4 - Passenger List" << endl;
        cout << "  0 - Exit System" << endl << endl;
        cin >> selection;
        switch(selection){
            case 1: mainFlight.newTicket();
            case 2: mainFlight.delTicket();
            case 3: mainFlight.checkTicket();
            case 4: mainFlight.printManifest();
            case 0: cout << "Thank you for using ATRP. Have a nice day.";
            default:cout << "Selection not recognized. Please try again." << endl;
        }
    } while(selection != 0);
    return 0;
}