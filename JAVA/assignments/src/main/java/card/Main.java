package card;

public class Main {
    public static void main(String[] args) {
        CardRepository repo = new CardRepository();
        CardController ctrl = new CardController(repo);

        CardRequest request1 = new CardRequest("Chat", "Cat");
        CardRequest request2 = new CardRequest("Chien", "Dog");
        CardRequest request3 = new CardRequest("Renard", "Fox");

        CardResponse response1 = ctrl.createCard(request1);
        CardResponse response2 = ctrl.createCard(request2);
        CardResponse response3 = ctrl.createCard(request3);

        System.out.println(response1);
        System.out.println(response2);
        System.out.println(response3);

        ctrl.showAllCards();
        ctrl.showCardById(1);
    }
}
