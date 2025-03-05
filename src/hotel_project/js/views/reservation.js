document.addEventListener('DOMContentLoaded', function () {

    // helper function to calculate the difference between two dates
    function datediff(first, second) {
        // Calculate the time difference in milliseconds
        const diffTime = Math.abs(second - first);
        // Convert the difference to days
        return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    }

    // Parse a date string into a Date object
    function parseDate(date) {
        if (!date) return null;
        
        try {
            return new Date(date);
        } catch (e) {
            console.error("Invalid date format:", date);
            return null;
        }
    }


    // Check if the current page is the reservation finish page
    if (location.pathname.includes('reservation/finish')) {
        // get the hotel and room data from the backend
        let url = window.location.href;
        let hotel = url.split('/')[5];
        let data = JSON.parse(sessionStorage.getItem('reservationData'));

        // check if the data is valid
        if (!data || !data.room || !data.checkIn || !data.checkOut) {
            console.error("Invalid reservation data:", data);
            return;
        }
        

        // assign the data to variables
        room = data.room;
        checkIn = data.checkIn;
        checkOut = data.checkOut;
        price = 0;

        if (document.getElementsByTagName('form').length > 0) {
            // fetch the hotel and room data
            fetch(`/api/hotel/${hotel}/room/${room}`)
                .then(response => response.json()
                    .then(data => {

                        // set the fetched data to the page
                        document.getElementById('hotel').innerText = data.hotel.name;
                        document.getElementById('start_date').innerText = checkIn;
                        document.getElementById('end_date').innerText = checkOut;
                        document.getElementById('room-type').innerText = data.room.room_type;
                        price = parseFloat(data.room.price.replace(/[^0-9.]/g, ''));
                        document.getElementById('total').innerText = price.toFixed(2);

                    // assign the values from the sessionstorage to the django form fields
                    const hotelField = document.getElementById('hotel_input');
                    if (hotelField) hotelField.value = hotel;
                    const roomField = document.getElementById('room_input');
                    if (roomField) roomField.value = room;
                    const startDateField = document.getElementById('start_date_input');
                    const endDateField = document.getElementById('end_date_input');
                    if (startDateField) startDateField.value = checkIn;
                    if (endDateField) endDateField.value = checkOut;
                    
                        // Parse dates and calculate total
                        const checkInDate = parseDate(checkIn);
                        const checkOutDate = parseDate(checkOut);
                        
                        // Calculate the total price
                        if (checkInDate && checkOutDate) {
                            const nights = datediff(checkInDate, checkOutDate);
                            document.getElementById('total').innerText = (nights * price).toFixed(2);
                            const priceField = document.getElementById('price_input');
                            if (priceField) priceField.value = (nights * price).toFixed(2);
                        } else {
                            document.getElementById('total').innerText = "Invalid dates";
                        }

                    })
                )
        }
    }
})
