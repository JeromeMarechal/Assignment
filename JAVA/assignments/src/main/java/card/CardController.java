package card;

public class CardController {
    private CardService service;

    public CardController(CardService service) {
        this.service = service;
    }

    public void showAllCards() {
        System.out.println("ALL CARDS");
        for (Card c : service.getAllCards()) {
            System.out.println(c);
        }
    }

    public void showCardById(int id) {
        System.out.println("FIND ID: " + id);
        Card c = service.getCardById(id);
        if (c != null) {
            System.out.println(c);
        }
    }


}
