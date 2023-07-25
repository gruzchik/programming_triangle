import java.util.ArrayList;
import java.util.Scanner;

class Main {
  private static ArrayList<String> cities = new ArrayList<>();
  private static Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) {
    fillCities();
    gameLoop();

    String input = scanner.nextLine();
    System.out.println("input: " + input);
  }

  private static void gameLoop() {
    while (true) {
      String input = scanner.nextLine();

      if (input.equals("exit")) {
        System.out.println("Дякую за гру!");
        System.exit(0);
      }
      char lastChar = input.charAt(input.length() - 1);
      // System.out.println("Last char: " + lastChar);
      for (String city : cities) {
        char firstChar = city.charAt(0);

        if (Character.toLowerCase(lastChar) == Character.toLowerCase(firstChar)) {
          System.out.println("Моє місто: " + city);
          break;
        }
      }
    }
  }

  private static void fillCities() {
    cities.add("Київ");
    cities.add("Вінниця");
    cities.add("Харків");
    cities.add("Полтава");
    cities.add("Львів");
    cities.add("Конотоп");
    cities.add("Дніпро");
    cities.add("Чернігів");
    cities.add("Одеса");
    cities.add("Авдіївка");
    cities.add("Ялта");
  }
}