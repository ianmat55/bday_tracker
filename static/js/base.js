
window.onload = function() {
	const target = document.getElementById('data');
	const toggle = document.getElementById('toggle')

	toggle.onclick = function () {
		if (target.style.display !== "none") {
			target.style.display = "none";
			target.style.margin = "auto";
		} else {
			target.style.display = "flex";
			target.style.justifyContent = "center";
			target.style.alignItems = "center";
		}
	};
};