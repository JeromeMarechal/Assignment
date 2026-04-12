package card;
import java.util.List;
import java.util.ArrayList;

public class CardRepository {
    private List<Card> database = new ArrayList<>();

    public CardRepository() {
        database.add(new Card(1, "chien", "dog"));
        database.add(new Card(2, "chat", "cat"));
        database.add(new Card(3, "humain", "human"));
    }

    public List<Card> getAll() {
        return database;
    }

    public Card getById(int id) {
        for (Card c : database) {
            if (c.getId() == id) {
                return c;
            }
        }
        return null;
    }
}
