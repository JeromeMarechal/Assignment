package card;

public class CardResponse {
    private int id;
    private String word;
    private String translation;

    public CardResponse (int id, String word, String translation) {
        this.id = id;
        this.word = word;
        this.translation = translation;
    }

    public int getId() {
        return this.id;
    }

    public String getWord() {
        return this.word;
    }

    public String getTranslation() {
        return this.translation;
    }

    @Override
    public String toString() {
        return "Card :" + id + " | " + word + " = " + translation + ".";
    }
}
