document.addEventListener('DOMContentLoaded', function() {
    //handle room div click and pagination
    document.addEventListener('click', function(e) {
        const hotelCard = e.target.closest('.hotel-card');
        // if a hotel card is clicked, navigate to the hotel details page
        if (hotelCard) {
            // get the hotel id from the dataset
            const hotelId = hotelCard.dataset.hotelId;
            // navigate to the hotel details page
            window.location.href = `/hotel/${hotelId}`;
        }

    });

});
