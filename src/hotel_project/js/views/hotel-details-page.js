document.addEventListener('DOMContentLoaded', function() {
    // handle room selection
    document.addEventListener('change', function(e) {
        if (e.target.classList.contains('hotel-page__input')) {
            const selectedRoomPrice = e.target.value;

            //update the price on the page
            document.querySelector('.hotel-page__room__price').textContent = selectedRoomPrice;
            
            // Enable book button when a room is selected and disable it when no room is selected
            const bookButton = document.querySelector('.hotel-page__button.hotel-page__button--primary');
            if (selectedRoomPrice && selectedRoomPrice !== '0') {
                bookButton.disabled = false;
            } else {
                bookButton.disabled = true;
            }
        }
    });
});