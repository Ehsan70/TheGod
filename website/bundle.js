(({document, fetch}) => {
  /**
   * Adds a css class to a DOM Element
   * @param {DOM Element} Element
   * @param {string} className
   * @return {DOM Element}
   */
  function addClass(Element, className) {
    const current = Element.className.split(' ')
    if (current.indexOf(className) < -1) {
      return Element
    }

    current.push(className)
    Element.className = current.join(' ')
    return Element
  }

  /**
   * Removes a css class from a DOM Element
   * @param  {DOM Element} Element
   * @param  {string} className
   * @return {DOM Element}
   */
  function removeClass(Element, className) {
    const current = Element.className.split(' ')
    if (current.indexOf(className) === -1) {
      return Element
    }

    current.splice(current.indexOf(className), 1)
    Element.className = current.join(' ')
  }

  /**
   * Binds an element with utility functions
   * @param  {DOM Element} Element
   * @return {DOM Element}
   */
  function $(Element) {
    Element.addClass = addClass.bind(null, Element)
    Element.removeClass = removeClass.bind(null, Element)
    return Element
  }

  /**
   * Updates DOM list
   * @param  {Collection} items
   * @return {Collection}
   */
  function renderItems(items) {
    while(Items.hasChildNodes()) {
      Items.removeChild(Items.lastChild)
    }

    items.map( item => {
      const el = document.createElement('div')
      el.innerHTML = item.MessageId.S
      Items.appendChild(el)
    })

    return items
  }

  /**
   * Renders error message to DOM
   * @param  {string} err
   */
  function renderError(err) {
    TheError.style.display = 'block'
    TheError.innerHTML = err
  }

  /**
   * Hides error message
   */
  function hideError() {
    TheError.style.display = 'none'
    TheError.innerHTML = ''
  }

  /**
   * Gets URL for async requests
   * @param  {DOM Form} form
   * @return {string}
   */
  function getUrl(form) {
    return form.action + '?TableName=' + form.TableName.value
  }

  /**
   * Makes request for Items
   * @return {Promise}
   */
  function loadItems() {
    const url = getUrl(Form)
    Button.addClass('is-loading')

    return fetch(url)
      .then( response => response.json() )
      .then( response => response.Items )
      .then( renderItems )
      .catch( renderError )
      .then( () => {
        Button.removeClass('is-loading')
      })
  }

  /**
   * Adds an item to the list
   * @param {string} table
   * @param {string} item
   * @return {Promise}
   */
  function addItem(table, item) {
    const payload = {
      TableName: table,
      Item: {
        MessageId: {S: item}
      }
    }

    return fetch(getUrl(Form), {
      method: 'POST',
      body: JSON.stringify(payload)
    })
  }


  const messages_div = document.getElementById('messages');

  var request = new XMLHttpRequest();
  // Todo make the below URL configurable
  request.open('GET', 'https://6pz092slz6.execute-api.us-east-1.amazonaws.com/TG-DevStage/messages', true);
  request.onload = function () {
    // Begin accessing JSON data here
    var data = JSON.parse(this.response);
    console.log("Data from database is "+ JSON.stringify(data))

    if (request.status >= 200 && request.status < 400) {
      // If success 
      console.log("items are "+ JSON.stringify(data["Items"]))

      data["Items"].forEach(msg => {
        const msg_p = document.createElement('p');
        msg_p.textContent = msg.Value;
        messages_div.appendChild(msg_p)
      });
    } else {
      const errorMessage = document.createElement('marquee');
      errorMessage.textContent = `Gah, it's not working! Cannot get the messages from database.`;
      messages_div.appendChild(errorMessage);
    }
  }
  
  request.send();

})({document, fetch})

