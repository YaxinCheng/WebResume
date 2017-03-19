import Vapor

let drop = Droplet()

drop.get { req in
    return try drop.view.make("index", ["category": "overview"])
}

drop.get("skill") { req in
	return try drop.view.make("index", ["category": "skill"])
}

drop.get("projects") { req in
	return try drop.view.make("index", ["category": "projects"])
}

drop.get("experience") { req in
	return try drop.view.make("index", ["category": "experience"])
}

drop.get("contact") { req in
	return try drop.view.make("index", ["category": "contact"])
}

drop.get("overview") { req in
	return try drop.view.make("index", ["category": "overview"])
}
drop.run()
