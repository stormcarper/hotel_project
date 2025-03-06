import flatpickr from "flatpickr";

document.addEventListener('DOMContentLoaded', function () {
    // Check if the current page is the reservation date page
    if (this.location.pathname.includes('reservation/date')) {
        // get the room_id form the url
        const room = this.location.pathname.split('/')[4];
        const startDate = document.getElementById('start_date')
        const endDate = document.getElementById('end_date')

        flatpickr(startDate, {
            inline: true,
            dateFormat: "Y-m-d",
            minDate: "today",
            maxDate: new Date().fp_incr(1095)
        });

        flatpickr(endDate, {
            inline: true,
            dateFormat: "Y-m-d",
            minDate: "today",
            maxDate: new Date().fp_incr(1095)
        })
        // add an click event listener on the submit button
        document.getElementById('submit_date').addEventListener('click', function () {
            // select the check-in and check-out date
            let checkIn = document.getElementById('start_date').value;
            let checkOut = document.getElementById('end_date').value;

            //get hotel url from the current page
            let url = window.location.href;
            let hotel = url.split('/')[5];

            // check for empty fields
            if (!room || !checkIn || !checkOut) {
                let alert = document.getElementById('reservation__alert');
                alert.innerText = "Please fill in all fields";
                alert.style.display = 'block';
                return;
            }

            // check if checkin is before checkout
            if (checkIn >= checkOut) {
                let alert = document.getElementById('reservation__alert');
                alert.innerText = "Check-out date must be after check-in date";
                alert.style.display = 'block';
                return;
            }

            // check if the reservation is in the future
            let currentDate = new Date();
            let checkInDate = new Date(checkIn);
            let checkOutDate = new Date(checkOut);
            if (checkInDate < currentDate || checkOutDate < currentDate) {
                let alert = document.getElementById('reservation__alert');
                alert.innerText = "Check-in and check-out dates must be in the future";
                alert.style.display = 'block';
                return;
            }


            // Store reservation data in sessionStorage
            sessionStorage.setItem('reservationData', JSON.stringify({
                room: room,
                checkIn: checkIn,
                checkOut: checkOut
            }));

            // Redirect to the next page
            window.location.href = `/reservation/finish/${hotel}`;
        })
    }
})