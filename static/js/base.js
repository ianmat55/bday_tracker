
window.onload = function() {
	const target = document.getElementById('data');
	const toggle = document.getElementById('toggle');
	

	toggle.onclick = function() {
		if (target.style.display !== "none") {
			target.style.display = "none";

		} else {
			target.style.display = "flex";
	
		}
	};

};