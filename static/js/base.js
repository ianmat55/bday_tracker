
window.onload = function() {
	const target = document.getElementById('data');
	const toggle = document.getElementById('toggle');
	const update_toggle = document.getElementById('update_toggle');
	const update_target = document.getElementById('updateform');
	const delete_toggle = document.getElementById('delete_toggle');
	const delete_target = document.getElementById('deleteform');

	toggle.onclick = function() {
		if (target.style.display !== "none") {
			target.style.display = "none";

		} else {
			target.style.display = "flex";
	
		}
	};

	update_toggle.onclick = function() {
		if (update_target.style.display !== "none") {
			update_target.style.display = "none";

		} else {
			update_target.style.display = "flex";
	
		}
	}

	delete_toggle.onclick = function() {
		if (delete_target.style.display !== "none") {
			delete_target.style.display = "none";

		} else {
			delete_target.style.display = "flex";
	
		}
	}
};