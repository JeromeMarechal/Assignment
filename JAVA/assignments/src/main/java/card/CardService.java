package card;
import java.util.List;

public class CardService {
    private CardRepository repository;

    public CardService(CardRepository repository) {
        this.repository = repository;
    }

    public List<Card> getAllCards() {
        return repository.getAll();
    }

    public Card getCardById(int id) {
        Card c = repository.getById(id);
        if (c == null) {
            System.out.println("Card not found");
        }
        return c;
    }
}
