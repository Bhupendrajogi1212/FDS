#include <iostream>
using namespace std;

class queue {
  int queue1[5];   // VARIABLE TO INSERT ELEMENT (data)
  int rear, front; // variable
                   //  rear and front

public:
  queue() // constructor
  {
    rear = -1;
    front = -1;
  }

  void insertjob(int x) {
    if (rear > 4) // check queue is full or not
    {
      cout << "QUEUE OVERFLOW";
      front = rear = -1;
      return;
    }

    queue1[++rear] = x;
    cout << "INSERTED - " << x;
  }

  void deletejob() {
    if (front == rear)

    {
      cout << "QUEUE UNDERFLOW";
      return;
    }
    cout << "DELETED - " << queue1[++front];
  }

  void display() {
    if (rear == front) {
      cout << " QUEUE EMPTY";
      return;
    }

    for (int i = front + 1; i <= rear; i++)
      cout << queue1[i] << " ";
  }
};

int main() {
  int ch;   // choice variable
  queue qu; // object of class (instance)

  while (1) {
    cout << "\n\n**************PRACTICAL NO-13(E-29) JOB QUEUE***************";
    cout << "\n1.INSERT_JOB \n2.DELETE_JOB \n3.DISPLAY \n4.EXIT\nENTER THE "
            "CHOICE :";
    cin >> ch;

    switch (ch) {
    case 1:
      cout << "ENTER ORDER ID:"; // insert element 
      cin >> ch;
      qu.insertjob(ch);
      break;

    case 2:
      qu.deletejob();
      break;

    case 3:
      qu.display();
      break;

    case 4:
      return (0);
    }
  }
  return (0);
}
