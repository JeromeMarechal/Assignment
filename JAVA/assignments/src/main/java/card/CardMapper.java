package card;

public class CardMapper {
    public static Card toCard (CardRequest request, int id) {
        return new Card (
            id,
            request.getWord(),
            request.getTranslation()
        );
    }

    public static CardResponse toResponse (Card card) {
        return new CardResponse (
            card.getId(),
            card.getWord(),
            card.getTranslation()
        );
    }
}
