// Stripe Payment Code

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var card = elements.create('card', { style: style });
var style = {
    base: {
        color: '#000',
        fontFamily: '"Lato",sans-serif;',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4',
        }

    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545',
    }
};
card.mount('#card-element');

// Validation handleing
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
        <span role="alert">
            <i class="fas fa-times"></i>
        </span>
        <span>${event.error.message}</span>`;

        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

//Accepting a payment sourced form stripe official docs

// Create a token or display an error when the form is submitted.
const form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true)

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
            <span role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${result.error.message}</span>`;
    
            $(errorDiv).html(html);
            card.update({'disabled': false});
            $('#submit-button').attr('disabled', false)
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});

// const {token, error} = await stripe.createToken(card);

//   if (error) {
//     // Inform the customer that there was an error.
//     const errorElement = document.getElementById('card-errors');
//     errorElement.textContent = error.message;
//   } else {
//     // Send the token to your server.
//     stripeTokenHandler(token); v 

//   }