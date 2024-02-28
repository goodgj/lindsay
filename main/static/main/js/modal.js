$('.js-btn-modal').on('click', function(){
  $('.modaler-content').fadeIn();
  $('#modaler').fadeIn();
  var id = $(this).data('id');
  $('.js-modal[data-id="hbxmodal' + id + '"]').fadeIn();
});

$('.close').on('click', function(){
  $('#modaler').fadeOut();
  $('.js-modal').fadeOut();
  $('.modaler-content').fadeOut();
});
$('#modaler').on('click', function(){
  $('.js-modal').fadeOut();
  $('#modaler').fadeOut();
  $('.modaler-content').fadeOut();
});
$('.js-modal').on('click', function(){
  $('#modaler').fadeOut();
  $('.js-modal').fadeOut();
  $('.modaler-content').fadeOut();
});
