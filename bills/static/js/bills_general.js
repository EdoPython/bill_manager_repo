$(document).ready(function () {
    $('#bills_table').DataTable();
    $('.dataTables_length').addClass('bs-select');

    function calc_total() {
        var sum = 0.00;
        $('.amount').each(function(){
            var amount = parseFloat($(this).attr('amount')) * 100;
            sum += amount;
        });
        sum = sum / 100;
        $('#total_shown').text("Total Shown : " + sum.toString() + " €");
    }
    calc_total();

    $('.pagination li').click(calc_total());

    $('.delete_bill').on('click', function(){
        var delete_url = $(this).attr('url_delete');
        $.confirm({
            title: 'Delete bill',
            content: 'Are you sure you want to delete this bill?',
            type: 'red',
            typeAnimated: true,
            autoClose: 'cancel|10000',
            buttons: {
                confirm: {
                    text: 'Delete bill',
                    btnClass: 'btn-red',
                    action:function () {
                        return $.ajax({
                            url: delete_url,
                            dataType: 'json',
                            method: 'get'
                        }).done(function (response) {
                            if (response.is_deleted) {
                                $.alert('Bill deleted');
                                location.reload();
                            }
                            else {
                                $.alert('Error deleting the bill')
                            }
                        }).fail(function(){
                            $.alert('Something went wrong');
                        });
                    }
                },
                cancel: function () {}
            }
        });
    });
});