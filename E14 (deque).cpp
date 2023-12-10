#include <iostream>
using namespace std;
#define SIZE 10 // Change array size to 10

class dequeue {
  int a[SIZE], front, rear;

public:
  dequeue();
  void add_at_beg(int);
  void add_at_end(int);
  void delete_fr_front();
  void delete_fr_rear();
  void display();
};

dequeue::dequeue() {
  front = -1;
  rear = -1;
}

void dequeue::add_at_end(int item) {
  if (rear >= SIZE - 1) {
    cout << "\n INSERTION IS NOT POSSIBLE, OVERFLOW!!!!";
  } else {
    if (front == -1) {
      front++;
      rear++;
    } else {
      rear = rear + 1;
    }
    a[rear] = item;
    cout << "\n INSERTED ITEM IS :" << a[rear];
  }
}

void dequeue::add_at_beg(int item) {
  if (front == -1) {
    front = 0;
    a[++rear] = item;
    cout << "\n INSERTED ELEMENT IS :" << item;
  } else if (front != 0) {
    a[--front] = item;
    cout << "\n INSERTED ELEMENT IS :" << item;
  } else {
    cout << "\n INSERTION IS NOT POSSIBLE, OVERFLOW!!!";
  }
}

void dequeue::display() {
  if (front == -1) {
    cout << "DEQUEUE IS EMPTY";
  } else {
    for (int i = front; i <= rear; i++) {
      cout << a[i] << " ";
    }
    cout << endl;
  }
}

void dequeue::delete_fr_front() {
  if (front == -1) {
    cout << "DELETION IS NOT POSSIBLE::DEQUEUE IS EMPTY";
    return;
  } else {
    cout << "THE DELETED ELEMENT IS :" << a[front];
    if (front == rear) {
      front = rear = -1;
    } else
      front = front + 1;
  }
}

void dequeue::delete_fr_rear() {
  if (front == -1) {
    cout << "DELETION IS NOT POSSIBLE::DEQUEUE IS EMPTY";
    return;
  } else {
    cout << "THE DELETED ELEMENT IS : " << a[rear];
    if (front == rear) {
      front = rear = -1;
    } else
      rear = rear - 1;
  }
}

int main() {
  int c, item;
  dequeue d1;
  do {
    cout << "\n\n*****************PRACTICAL NO-14(E-31) "
            "DEQUEUE*****************\n";
    cout << "\n 1 INSERT AT START";
    cout << "\n 2 INSERT AT END";
    cout << "\n 3 DISPLAY";
    cout << "\n 4 DELETE FROM FRONT";
    cout << "\n 5 DELETE FROM REAR";
    cout << "\n 6 EXIT";
    cout << "\n ENTER YOUR CHOICE : ";

    cin >> c;

    switch (c) {
    case 1:
      cout << "ENTER THE ELEMENT IS TO BE INSERTED :";
      cin >> item;
      d1.add_at_beg(item);
      break; // Add a break statement here

    case 2:
      cout << "ENTER THE ELEMENT IS TO BE INSERTED :";
      cin >> item;
      d1.add_at_end(item);
      break;

    case 3:
      d1.display();
      break;

    case 4:
      d1.delete_fr_front();
      break;

    case 5:
      d1.delete_fr_rear();
      break;

    case 6:
      exit(1);
      break;
    default:
      cout << "INVALID CHOICE!!!!!";
      break;
    }
  } while (c != 6); // Change the condition here
  return 0;
}
