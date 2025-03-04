document.addEventListener('DOMContentLoaded', function() {

    if (window.location.pathname.includes('hotel/')) {
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

        // handle order submission
        document.getElementById('hotel-page__button').addEventListener('click', function() {
            let room = document.querySelector('.hotel-page__input');
            let price = room.value;
            let room_id = room.options[room.selectedIndex].getAttribute('room_id');
            console.log(room_id);
            console.log(price);
            let alert = document.querySelector('.hotel-page__alert');
            let hotel = window.location.pathname.split('/')[2];
            if (!price) {
                alert.textContent = 'Please select a room';
                alert.style.display = 'block';
                return;
            } else {
                alert.style.display = 'none';
                window.location.href = `/reservation/date/${hotel}/${room_id}`;
            }

        });
    }
});