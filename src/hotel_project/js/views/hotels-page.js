document.addEventListener('DOMContentLoaded', function() {
    //handle room div click
    document.addEventListener('click', function(e) {
        const hotelCard = e.target.closest('.hotel-card');
        // if a hotel card is clicked, navigate to the hotel details page
        if (hotelCard) {
            console.log('hotel card clicked');
            // get the hotel id from the dataset
            const hotelId = hotelCard.dataset.hotelId;
            console.log(hotelId);
            window.location.href = `/hotel/${hotelId}`;
        }
    })
});