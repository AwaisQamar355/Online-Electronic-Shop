        class MyClass {
            constructor(element) {
                this._element = element;
            }

            isAnimated = () => {
                return this._element.classList.contains('alii');
            }
        }

        // Usage
        document.addEventListener('DOMContentLoaded', () => {
            const modalElements = document.querySelectorAll('.modal-2');
            modalElements.forEach(element => {
                const myInstance = new MyClass(element);
                console.log(myInstance.isAnimated());
            });
        });