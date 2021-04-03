class ShopList {
    constructor(container, counter, api) {
        this.container = container;
        this.counter = counter;
        this.api = api;
        this.delItem = this.delItem.bind(this)
    }
    addEvent(){
        this.container.addEventListener('click', this.delItem)
    }
    delItem (e) {
        const target = e.target;
        if(target.classList.contains('shopping-list__button')) {
            const item = target.closest('.shopping-list__item');
            const download_button = document.getElementById('download_button')
            this.api.removePurchases(item.getAttribute('data-id'))
                .then( e => {
                    item.remove();
                    this.counter.minusCounter();

                    if (this.counter.counterNum == 0) {
                        download_button.hidden = true
                    }
                })
                .catch( e => {
                    console.log(e)
                })
        }
    }
}
