package org.example;

public class Animal {
    private String name;
    private String species;
    private char gender;
    private int age;

    public Animal(String name, String species, char gender, int age) {
        this.name = name;
        this.species = species;
        this.gender = gender;
        this.age = age;
    }

    public void setAge(int age) {
        if (age >= 0) {
            this.age = age;
        } else {
            System.out.println("ERROR: l'âge ne peut pas être négatif !!");
            this.age = 0;
        }
    }

    public void setGender(char gender) {
        if (gender == 'M' || gender == 'F') {
            this.gender = gender;
        } else {
            gender = 'Z';
        }
    }

    public String getProfile() {
        return String.format("Voici un magnifique " + species + " de " + age + " ans, (" + gender + ") qui se prénomme " + name + ".");
    }
}
