package card;

public class Card {
    private int id;
    private String word;
    private String translation;

    public Card(int id, String word, String translation) {
        this.id = id;
        this.word = word;
        this.translation = translation;
    }

    public int getId() {
        return id;
    }

    public String getWord() {
        return word;
    }

    public String getTranslation() {
        return translation;
    }

    @Override
    public String toString() {
        return "(" + id + ") " + word + ": " + translation;
    }
}
