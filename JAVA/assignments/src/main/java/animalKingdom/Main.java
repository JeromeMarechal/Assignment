package animalKingdom;

public class Main {
    static void main() {
        Animal lion = new Animal("Simba", "Félin", Genre.MALE, 15);
        System.out.println(lion.getProfile());
    }
}
