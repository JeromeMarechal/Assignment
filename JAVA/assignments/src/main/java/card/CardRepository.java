package card;
import java.util.List;
import java.util.ArrayList;

public class CardRepository {
    private List<Card> database = new ArrayList<>();
    private int currentId = 1;

    public Card save (Card card) {
        System.out.println("Ssving card in database ...");

        Card savedCard = new Card (
            currentId++,
            card.getWord(),
            card.getTranslation()
        );

        database.add(savedCard);

        System.out.println("Card saved with ID : " + savedCard.getId());
        return savedCard;
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
