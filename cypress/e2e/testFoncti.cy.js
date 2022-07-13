describe('empty spec', () => {
  it('Validation de la page', () => {
    cy.visit('http://localhost:8501')
    cy.get('input').eq(0).clear().type('100').type('{enter}')
    cy.get('input').eq(1).clear().type('2').type('{enter}')
    cy.get('input').eq(2).clear().type('0').type('{enter}')

    cy.get('input').eq(0).type('123').invoke('val').should(value => {
    expect(Number.isInteger(+value), 'input should be an integer').to.eq(true) // passes
    })

    cy.get('p').then((valeur) => {
      var val = parseFloat(valeur[0].innerText.substr(27))

      expect(val).to.be.greaterThan(10000)

    })



  })
})