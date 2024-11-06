#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>

using namespace std;



int LT_index = 0; // index of LT table
int ST_index = 0; // index of ST table  
int add = 0; // address in source code

// MOT Map: Mapping mnemonics to codes
map<string, string> MOT = {
    {"STOP", "00"}, {"ADD", "01"}, {"SUB", "02"}, {"MULT", "03"}, {"MOVER", "04"},
    {"MOVEM", "05"}, {"COMP", "06"}, {"BC", "07"}, {"DIV", "08"}, {"READ", "09"},
    {"PRINT", "10"}, {"START", "01"}, {"END", "02"}, {"ORIGIN", "03"}, {"LTORG", "05"},
    {"DS", "01"}, {"DC", "02"}, {"AREG,", "01"}, {"BREG,", "02"}, {"EQ", "01"}
};

// Structure for symbol and literal tables
struct TableEntry {
    int index;
    string symbol;
    int address;
};

vector<TableEntry> ST; // Symbol Table
vector<TableEntry> LT; // Literal Table
vector<vector<pair<string, int>>> code; // Intermediate code table
ifstream source;

// Function to classify the class of a word in the Intermediate table
string classy(const string& text) {
    string upper_text = text;
    transform(upper_text.begin(), upper_text.end(), upper_text.begin(), ::toupper);

    if (MOT.count(upper_text)) {
        if (upper_text == "START" || upper_text == "END" || upper_text == "ORIGIN" || upper_text == "LTORG") return "AD";
        if (upper_text == "DS" || upper_text == "DC") return "DL";
        if (upper_text == "AREG," || upper_text == "BREG,") return "RG";
        return "IS";
    }
    return "None";
}

// Function to handle START directive and get the starting address
int handle_start() {
    string line;
    if (!getline(source, line)) {
        cout << "No Start Statement! Abort!\n";
        return 0;
    }
    
    istringstream iss(line);
    vector<string> words;
    string word;
    while (iss >> word) words.push_back(word);

    if (words[0] == "START") {
        return stoi(words[1]);
    } else {
        cout << "No Start Statement! Abort!\n";
        return 0;
    }
}

// Pass 1 function
void pass1() {
    add = handle_start();
    if (!add) {
        cout << "Ending Pass 1 due to Above error.\n";
        return;
    }

    string line;
    while (getline(source, line)) {
        vector<string> words;
        istringstream iss(line);
        for (string word; iss >> word;) words.push_back(word);

        for (auto& w : words) {
            transform(w.begin(), w.end(), w.begin(), ::toupper);

            if (w[0] == '=') {
                LT.push_back({LT_index++, w, add});
            } else if (classy(w) == "None") {
                bool exists = false;
                for (auto& term : ST) {
                    if (term.symbol == w) {
                        exists = true;
                        break;
                    }
                }
                if (!exists) ST.push_back({ST_index++, w, add});
            }
        }
        add++;
    }

    cout << "LT:\n";
    for (auto& entry : LT) cout << entry.index << " " << entry.symbol << " " << entry.address << endl;

    cout << "\n\nST:\n";
    for (auto& entry : ST) cout << entry.index << " " << entry.symbol << " " << entry.address << endl;
}

// Pass 2 function
void pass2() {
    source.clear();
    source.seekg(0, ios::beg);

    string line;
    while (getline(source, line)) {
        vector<pair<string, int>> entry;
        vector<string> words;
        istringstream iss(line);
        for (string word; iss >> word;) words.push_back(word);

        for (auto& w : words) {
            transform(w.begin(), w.end(), w.begin(), ::toupper);
            if (classy(w) != "None") {
                entry.push_back({classy(w), stoi(MOT[w])});
            } else if (w[0] == '=') { // it is a literal
                for (auto& lt_entry : LT) {
                    if (lt_entry.symbol == w) {
                        entry.push_back({"L", lt_entry.index});
                        break;
                    }
                }
            } else { // it is a symbol
                for (auto& st_entry : ST) {
                    if (st_entry.symbol == w) {
                        entry.push_back({"S", st_entry.index});
                        break;
                    }
                }
            }
        }
        code.push_back(entry);
    }

    cout << "\n\nPASS 2:\nThe Intermediate code is:\n";
    for (auto& entry : code) {
        for (auto& elem : entry) {
            cout << "(" << elem.first << "," << elem.second << ") ";
        }
        cout << endl;
    }
}

int main() {
    source.open("source.txt");
    if (!source) {
        cerr << "File Not found. Create a source.txt first!\n\n\n";
        return 1;
    }

    cout << "File read successfully \n\n";
    pass1();
    pass2();

    source.close();
    return 0;
}