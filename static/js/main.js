$('#bar').click(function(){
    $(this).toggleClass('open');
    $('#page-content-wrapper ,#sidebar-wrapper').toggleClass('toggled' );

});



$(document).ready( function () {
    $('table.displayTable').DataTable({
        select: true,
        lengthMenu: [[5,10, 25, 50, -1], [5,10, 25, 50, "All"]],
        // serverSide: true,
        deferRender: true,
        scrollY:        '25vh',
        scrollCollapse: false,
        paging:         true,
        dom: 'Blfrtip',
        columnDefs: [
            {
                targets: 1,
                className: 'noVis'
            }
        ],
        buttons: [
            {
                extend: 'colvis',
                columns: ':not(.noVis)',
                text:'Select Columns'
                
            },
            {
                extend: 'collection',
                text: 'Download',
                buttons: [
                    {
                        text: 'Copy',
                        extend:'copy',
                        exportOptions: {
                            columns: [ 0, ':visible' ]
                        }
                        
                    },
                    {
                        text: 'CSV',
                        extend:'csv',
                        exportOptions: {
                            columns: [ 0, ':visible' ]
                        }
                        
                    },
                    {
                        text: 'Excel',
                        extend:'excel',
                        exportOptions: {
                            columns: [ 0, ':visible' ]
                        }
                        
                    },
                    {
                        text: 'PDF',
                        extend:'pdf',
                        exportOptions: {
                            columns: [ 0, ':visible' ]
                        }
                        
                    },
                    {
                        text: 'Print',
                        extend:'print',
                        exportOptions: {
                            columns: [ 0, ':visible' ]
                        }
                        
                    },

                ]
            }
        ]

});
} );
$(document).ready( function () {
    $('table.displayTableNoCol').DataTable({
        select: true,
        lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
        // serverSide: true,
        deferRender: true,
        scrollY:        '50vh',
        scrollCollapse: false,
        paging:         true,
        dom: 'Blfrtip',
        columnDefs: [
            {
                targets: 1,
                className: 'noVis'
            }
        ],
        buttons: [
        ]

});
} );



$(document).ready( function () {
    $('table.FullPageDisplayTable').DataTable({
        fixedHeader: true,
        select: true,
        lengthMenu: [[20, 50, 100, -1], [20, 50, 100, "All"]],
        scrollY:        '60vh',
        scrollCollapse: false,
        paging:         true,
        dom: 'Blfrtip',
        columnDefs: [
            {
                targets: 1,
                className: 'noVis'
            }
        ],
        buttons: [
            {
                extend: 'colvis',
                columns: ':not(.noVis)',
                text:'Select Columns'
                
            },
            {
                extend: 'collection',
                text: 'Download',
                buttons: [
                    {
                        text: 'Copy',
                        extend:'copy',
                        exportOptions: {
                            columns: [ 0, ':visible' ]
                        }
                        
                    },
                    {
                        text: 'CSV',
                        extend:'csv',
                        exportOptions: {
                            columns: [ 0, ':visible' ]
                        }
                        
                    },
                    {
                        text: 'Excel',
                        extend:'excel',
                        exportOptions: {
                            columns: [ 0, ':visible' ]
                        }
                        
                    },
                    {
                        text: 'PDF',
                        extend:'pdf',
                        exportOptions: {
                            columns: [ 0, ':visible' ]
                        }
                        
                    },
                    {
                        text: 'Print',
                        extend:'print',
                        exportOptions: {
                            columns: [ 0, ':visible' ]
                        }
                        
                    },

                ]
            }
        ]

});
} );