package animalKingdom;

public class Animal {
    private final String name;
    private final String species;
    private Genre gender;
    private int age;

    public Animal(String name, String species, Genre gender, int age) {
        this.name = name;
        this.species = species;
        setAge(age);
        setGender(gender);
    }

    public void setAge(int age) {
        if (age < 0) {
            throw new IllegalArgumentException("Animal's age cannot be negative");
        }
        this.age = age;
    }

    public void setGender(Genre gender) {
        if (gender == null) {
            throw new IllegalArgumentException("Animal's gender cannot be null.");
        }
        this.gender = gender;
    }

    public String getProfile() {
        return String.format("Voici un magnifique %s de %d ans, %s, qui se prénomme %s", species, age, gender, name);
    }
}


