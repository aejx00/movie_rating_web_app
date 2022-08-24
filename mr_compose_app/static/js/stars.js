//ES6
$.fn.stars = function () {
    return $(this).each(function () {
        const rating = ($(this).data("rating")) / 2;
        const numStars = $(this).data("numStars");
        const fullStar = '<i class="text-warning fas fa-star"></i>'.repeat(Math.floor(rating));
        const halfStar = (rating % 1 !== 0) ? '<i class="text-warning fas fa-star-half-alt"></i>' : '';
        const noStar = '<i class="text-warning far fa-star"></i>'.repeat(Math.floor(numStars - rating));
        $(this).html(`${fullStar}${halfStar}${noStar}`);
    });
}