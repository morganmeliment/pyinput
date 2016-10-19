try:
	from browser import window, document
	from javascript import JSObject, JSConstructor

	jq = window.jQuery

	input_c = None

	def input_callback():
	    input_value = jq('#toInput').val()
	    jq('#toInput').val('')

	    input_t = jq('#toPrompt').text()
	    jq('#toPrompt').text('')
    
	    print(input_t + " " + input_value)
	    input_c(input_t, input_value)

	def input_fade(ev):
	    jq('.inputScreen').fadeOut(300, input_callback)
	    jq('#toSubmit').off('click')

	def input(text, callback):
	    jq('.inputScreen').fadeIn(300)
	    jq('#toPrompt').text(text)
    
	    global input_c
	    input_c = callback
	    jq('#toSubmit').on('click', input_fade)
except:
	underInput = input
	def input(text, callback):
		x = underInput(text+" ")
		callback(text, x)