package card;

public class CardController {
    private CardRepository repository;

    public CardController (CardRepository repository) {
        this.repository = repository;
    }

    public CardResponse createCard (CardRequest request) {
        System.out.println("Receiving request to create card...");

        Card card = CardMapper.toCard(request, 0);
        Card savedCard = repository.save(card);
        CardResponse response = CardMapper.toResponse(savedCard);

        System.out.println("Returning response ....");
        return response;
    }

    public void showAllCards() {
        System.out.println("ALL CARDS");
        for (Card c : repository.getAll()) {
            System.out.println(c);
        }
    }

    public void showCardById(int id) {
        System.out.println("FIND ID: " + id);
        Card c = repository.getById(id);
        if (c != null) {
            System.out.println(c);
        }
    }
}
