#include <cstring>
#include <iostream>
using namespace std;

struct node {
  int prn;
  char name[20];
  node *next;
};

class pinnacle {
  node *head = NULL, *tail = NULL;

public:
  void create() {
    int data;
    char name1[20];
    node *temp = new node;
    cout << "ENTER THE PRN :";
    cin >> data;
    cout << "ENTER THE NAME :";
    cin >> name1;
    temp->prn = data;
    strcpy(temp->name, name1);
    temp->next = NULL;
    if (head == NULL) {
      head = temp;
      tail = temp;
    } else {
      tail->next = temp;
      tail = tail->next;
    }
  }

  void president() {
    int data;
    char name1[20];
    node *temp = new node;
    cout << "ENTER THE PRN :";
    cin >> data;
    cout << "ENTER THE NAME :";
    cin >> name1;
    temp->prn = data;
    strcpy(temp->name, name1);
    if (head == NULL) {
      head = temp;
    } else {
      temp->next = head;
      head = temp;
    }
  }

  void member() {
    int data, pos;
    node *mem;
    char name1[20];
    node *temp = new node;
    cout << "ENTER THE PRN :";
    cin >> data;
    cout << "ENTER THE NAME :";
    cin >> name1;
    temp->prn = data;
    strcpy(temp->name, name1);
    if (head == NULL) {
      head = temp;
      tail = temp;
    } else {
      cout << "ENTER THE POSITION AFTER WHICH YOU WANT TO INSERT :";
      cin >> pos;
      mem = head;
      do {
        if (mem->prn == pos) {
          temp->next = mem->next;
          mem->next = temp;
          break;
        } else {
          mem = mem->next;  // Corrected from mem->next;
        }
      } while (mem != NULL);
    }
  }

  void display() {
    node *print;
    print = head;
    while (print != NULL) {
      cout << print->prn << "--->" << print->name << "\t";
      print = print->next;
    }
  }

  void total() {
    int count = 0;
    if (head == NULL) {
      cout << "LIST IS EMPTY\n";
    } else {
      node *temp = head;  // Added to avoid modifying head
      while (temp != NULL) {
        count++;
        temp = temp->next;
      }
      cout << "TOTAL NUMBER OF NODES :" << count;
    }
  }

  void deletePresident() {
    if (head != NULL) {
      node *temp = head;
      head = head->next;
      delete temp;
    }
  }

  void deleteMember() {
    int pos;
    cout << "ENTER THE POSITION AFTER WHICH YOU WANT TO DELETE :";
    cin >> pos;
    node *current = head;
    node *prev = NULL;

    for (int i = 0; i < pos && current != NULL; i++) {
      prev = current;
      current = current->next;
    }

    if (prev != NULL && current != NULL) {
      prev->next = current->next;
      delete current;
    }
  }

  void deleteSecretary() {
    if (head != NULL) {
      node *current = head;
      node *prev = NULL;

      while (current->next != NULL) {
        prev = current;
        current = current->next;
      }

      if (prev != NULL) {
        tail = prev;
        tail->next = NULL;
        delete current;
      }
    }
  }
};

int main() {
  int ch, ch2, ch3;
  char ch1;
  pinnacle p;
  do {
    cout << "\n******PRACTICAL NO-08(C-19) PINNACLE CLUB******";
    cout << "\n\tMENU\t\n";
    cout << "1.CREATE\n";
    cout << "2.DISPLAY\n";
    cout << "3.INSERT MEMBER\n";
    cout << "4.TOTAL MEMBERS\n";
    cout << "5.DELETE\n";
    cout << "************************************************";
    cout << "\n ENTER YOUR CHOICE :";
    cin >> ch;

    switch (ch) {
      case 1:
        p.create();
        break;

      case 2:
        p.display();
        break;

      case 3:
        cout << "**********************\n";
        cout << "1.PRESIDENT\n";
        cout << "2.MEMBER\n";
        cout << "3.SECRETARY\n";
        cout << "ENTER YOUR CHOICE :";
        cin >> ch2;
        switch (ch2) {
          case 1:
            p.president();
            break;

          case 2:
            p.member();
            break;

          case 3:
            p.create();
            break;
        }
        break;

      case 4:
        p.total();
        break;

      case 5:
        cout << "**********************\n";
        cout << "1.PRESIDENT\n";
        cout << "2.MEMBER\n";
        cout << "3.SECRETARY\n";
        cout << "ENTER YOUR CHOICE :";
        cin >> ch3;
        switch (ch3) {
          case 1:
            p.deletePresident();
            break;

          case 2:
            p.deleteMember();
            break;

          case 3:
            p.deleteSecretary();
            break;
        }
        break;
    }

    cout<<"\nDO YOU WANT TO CONTINUE :";
    cin>>ch1;
  } while (ch1 == 'y' || ch1 == 'Y');
  return 0;
}
