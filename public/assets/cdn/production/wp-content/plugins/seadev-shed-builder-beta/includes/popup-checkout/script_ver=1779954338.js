jQuery( document ).ready( function( $ ) {
    if ( $( '.checkout-for-init' )[0] ) {
        $( '.state_select').addClass( 'form-control' );
        $( '.popup-billing-fields__field-wrapper .validate-required' ).each( function () {
            $( this ).find( 'select' ).prop( 'required', true );
        } );
    }

    /**
     * Handle simplify checkout with group buttons
     */
    if ( $( '.group-buttons' )[0] ) {
        $( '.woocommerce.single button.group-button' ).on( 'click', function ( e ) {
            $( '.group-buttons, .group-checkout-overlay' ).toggleClass( 'active' );
        } );
        $( document ).on( 'click', function ( e ) {
            const { target } = e;
            if ( target instanceof HTMLElement ) {
                const className = target.className; // DOMTokenList
                if ( className !== 'button alt group-button' ) {
                    $( '.group-buttons, .group-checkout-overlay' ).removeClass( 'active' );
                }
            }
        } );
    }
    
    $( document ).on( 'submit', 'form.cart', function ( e ) {
        let actionType = $( '.woocommerce.single .single_add_to_cart_button' ).attr( 'action-type' );
        if ( actionType === 'wc-quick-checkout' || actionType === undefined ) {
            e.preventDefault();
            var result      = {};
            $.each( $( 'form.cart' ).serializeArray(), function () {
                result[this.name.split( '-' ).join( '_' )] = this.value;
            } );
            $( 'button.submit-order' ).attr( 'data', window.btoa( JSON.stringify( result ) ) );
            $( '.checkout-for-init, .overlay' ).addClass( 'active' );
        }
    } );

    $( document ).on( 'click', '.popup-checkout-footer .cancel-order', function ( e ) {
        $( '.footer-checkout, .overlay' ).removeClass( 'active thankyou' );
        $( 'button[name="add-to-cart"]' ).removeClass( 'disabled' );
        $( 'button[name="add-to-cart"]' ).css( 'pointer-events', 'auto' );
    } );

    $( document ).on( 'submit', 'form.ajax-create-order', function ( e ) {
        e.preventDefault();
        var building    = $( 'button.submit-order' ).attr( 'data' );
        if( ! isValidBase64Data( building ) ) {
            $( '.popup-checkout-footer .cancel-order' ).trigger( 'click' );
            alert( 'Action failed due to an unexpected interruption while generating building details. Re-click the button to retry.' );
            return;
        }

        $( '.page-loading' ).addClass( 'active' );
        $( '.loading-message' ).html( 'Capturing building details. Due to internet connection, the process might take up to a dozen seconds. Good things take time. Thank you for your patience!' );
        var result     = {};
        var product_id = $( 'button.submit-order' ).attr( 'product' );
        let cookieKey  = window.location.hostname + '.productID-' + product_id;
        $.each( $( 'form.ajax-create-order' ).serializeArray(), function () {
            let key     = this.name;
            result[key] = this.value;
        } );
        
        // Dynamically collect all _wc_order_attribution_ fields using WooCommerce's native function
        // This ensures new fields added by WooCommerce are automatically captured
        if (typeof wc_order_attribution !== 'undefined' && typeof wc_order_attribution.getAttributionData === 'function') {
            var attributionData = wc_order_attribution.getAttributionData();
            
            // Map to _wc_order_attribution_ prefixed keys for backend
            if (attributionData) {
                for (var key in attributionData) {
                    if (attributionData.hasOwnProperty(key) && attributionData[key] !== null) {
                        result['_wc_order_attribution_' + key] = attributionData[key];
                    }
                }
            }
        }
        
        $.ajax( {
            type: 'post',
            url:  '/wp-admin/admin-ajax.php',
            data: $.extend({
                action:     'pop_up_checkout_create_order',
                building:   building,
                customer:   result,
                product_id: product_id,
            }, result),
            beforeSend: function(){
            
            },
            success: function( response ) {
                let message = response.message;
                const encodeData = window.btoa( JSON.stringify( [] ) );
                document.cookie = `${cookieKey}=${encodeData};path=/`;
                if ( response.order_source === 'backend' ) {
                    window.parent.location.href = response.order_url; 
                    message = '<div style="text-align: center" class="popup-checkout-thanks">The request created, redirecting to the request detail...</div>';
                    $( '.response-checkout' ).addClass( 'backend-thank-you' );
                }
                $( '.page-loading, .checkout-for-init' ).removeClass( 'active' );
                $( '.response-checkout' ).addClass( 'thankyou active' );
                $( '.response-checkout' ).html( message );
				if (response.has_data) {
					sentMailAfterOrder(response);
				}
            },
            error: function( jqXHR, textStatus, errorThrown ){
                console.log( 'The following error occured: ' + textStatus, errorThrown );
            }
        } )
        return false;
    } );

    $( document ).on( 'click', '.submit-order', function( e ){
        var email = $( 'input[name="billing_email"]' ).val();
        var pattern = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i
        if ( !pattern.test( email ) ) {
            alert( 'The email address is not valid!' );
            return false;
        }

        const formatType    = fr_shedpro.ssb_phone_number_format;
        const phone         = $( '#billing_phone' ).val().replace( /\D/g,'' );
        let validTotalNum = 10; 
        if( 'international' === formatType ) {
            validTotalNum = 11;
        } else if( 'local' === formatType ) {
            validTotalNum = 7;
        }
        if( '' === phone || phone.length !== validTotalNum ) {
            alert( 'The phone number is not valid!' );
            return false;
        }
        
    } );

    $( document ).on( 'click', '.products li a.add_to_cart_button', function( e ){
        $( '.page-loading' ).addClass( 'active' );
    } );

    /**
     * Sent mail after create order
     */
    function sentMailAfterOrder( response ) {
        $.ajax({
            type : 'post',
            url : '/wp-admin/admin-ajax.php',
            data : {
                action  : 'popup_checkout_sent_mail',
                response: response,
            }
        })
        return false;
    }

    /**
     * Check if the provided base64Data is a valid Base64-encoded string.
     *
     * @param {string} base64Data - The Base64-encoded string to validate.
     * @returns {boolean} - True if the provided data is a valid Base64-encoded string, false otherwise.
     */
    function isValidBase64Data( base64Data ) {
        if( undefined === base64Data || '' === base64Data || '' === base64Data.trim() ) {
            return false;
        }

        try {
            JSON.parse( window.atob( base64Data ) );
            
            return window.btoa( window.atob( base64Data ) ) === base64Data;
        } catch ( err ) {
            return false;
        }
    }

    $( document.body ).on( 'change', '.country_to_state', function() {
        $( 'select.country_select, select.state_select' ).each( function() {
            $( this ).select2( 'close')
        });
    });
} );