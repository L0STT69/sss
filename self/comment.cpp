#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <regex>

using namespace std;

string removeComments(const string &code) {
    // Regular expression to match both single-line and multi-line comments
    regex commentPattern(R"((\/\/[^\n]*)|\/\*.*?\*\/)");

    // Replace comments with an empty string
    return regex_replace(code, commentPattern, "");
}

int main() {
    string inputFileName = "input.cpp";  // Change this to your input file name
    string outputFileName = "output.cpp"; // Change this to your desired output file name

    ifstream inputFile(inputFileName);

    if (!inputFile.is_open()) {
        cerr << "Unable to open the input file." << endl;
        return 1;
    }

    stringstream buffer;
    buffer << inputFile.rdbuf();
    string code = buffer.str();

    inputFile.close();

    // Remove comments from the code
    string cleanedCode = removeComments(code);

    // Write the cleaned code to the output file
    ofstream outputFile(outputFileName);
    if (!outputFile.is_open()) {
        cerr << "Unable to open the output file." << endl;
        return 1;
    }

    outputFile << cleanedCode;
    outputFile.close();

    cout << "Comments removed successfully. Cleaned code saved to " << outputFileName << endl;

    return 0;
}
