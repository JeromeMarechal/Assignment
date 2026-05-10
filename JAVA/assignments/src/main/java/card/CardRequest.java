package card;

public class CardRequest {
    private String word;
    private String translation;

    public CardRequest (String word, String translation) {
        this.word = word;
        this.translation = translation;
    }

    public String getWord() {
        return this.word;
    }

    public String getTranslation() {
        return this.translation;
    }
}
