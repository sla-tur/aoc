#include <iostream>
#include <vector>
#include <string>
#include <regex>

std::vector<int> buttons;

void printMatches(std::string s, std::regex reg) {
  std::smatch matches;
  std::cout << std::boolalpha;
  while (std::regex_search(s, matches, reg)) {
    std::cout << "Matches found: " << matches.str();
    buttons.push_back(std::stoi(matches.str(2)));
    buttons.push_back(std::stoi(matches.str(3)));
    s = matches.suffix().str();
    std::cout << '\n';
  }
}

int main() {
  std::ios::sync_with_stdio(0);
  std::cin.tie(0);
  std::freopen("aoc2024day13test.txt", "r", stdin);

  std::string s;
  //s = "Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=8400, Y=5400";
  while (std::getline(std::cin, s)) {
    std::regex reg ("Button ([AB]): X\\+(\\d+), Y\\+(\\d+)");
    printMatches(s, reg);
    reg = ("Prize: X=(\\d+), Y=(\\d+)");
    printMatches(s, reg);
    std::cout << buttons[0] + buttons[1] << '\n';
  }
  return 0;
}