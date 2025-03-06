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
        const room = data.room;
        const checkIn = data.checkIn;
        const checkOut = data.checkOut;
        let price = 0;

        if (document.getElementsByTagName('form').length > 0) {
            // fetch the hotel and room data
            fetch(`/api/hotel/${hotel}/room/${room}`)
                .then(response => response.json()
                    .then(data => {

                        // set the fetched data to the page
                        document.querySelector('.reservation__hotel').innerText = data.hotel.name;
                        document.querySelector('.reservation__start_date').innerText = checkIn;
                        document.querySelector('.reservation__end_date').innerText = checkOut;
                        document.querySelector('.reservation__room_type').innerText = data.room.room_type;
                        price = parseFloat(data.room.price.replace(/[^0-9.]/g, ''));
                        document.querySelector('.reservation__total').innerText = price.toFixed(2);

                    // assign the values from the sessionstorage to the django form fields
                    const hotelField = document.querySelector('.reservation__form__hotel_input');
                    if (hotelField) hotelField.value = hotel;
                    const roomField = document.querySelector('.reservation__form__room_input');
                    if (roomField) roomField.value = room;
                    const startDateField = document.querySelector('.reservation__form__start_date_input');
                    const endDateField = document.querySelector('.reservation__form__end_date_input');
                    if (startDateField) startDateField.value = checkIn;
                    if (endDateField) endDateField.value = checkOut;
                    
                        // Parse dates and calculate total
                        const checkInDate = parseDate(checkIn);
                        const checkOutDate = parseDate(checkOut);
                        
                        // Calculate the total price
                        if (checkInDate && checkOutDate) {
                            const nights = datediff(checkInDate, checkOutDate);
                            document.querySelector('.reservation__total').innerText = (nights * price).toFixed(2);
                            const priceField = document.querySelector('.reservation__form__price_input');
                            if (priceField) priceField.value = (nights * price).toFixed(2);
                        } else {
                            document.querySelector('.reservation__total').innerText = "Invalid dates";
                        }

                    })
                )
        }
    }
})
