package card;

public class Main {
    public static void main(String[] args) {
        CardRepository repo = new CardRepository();
        CardService service = new CardService(repo);
        CardController controller = new CardController(service);


        controller.showAllCards();
        controller.showCardById(2);
    }
}
