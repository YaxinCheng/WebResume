import Vapor

let drop = Droplet()
let mongoDB = MongoDB()

drop.get { req in
	guard let cursor = mongoDB.cursor else {
		print("Database cannot be connected")
		throw Abort.badRequest
	}
	let data = cursor["overviewContent"]
	let information = Array(try data.find()).map({mongoDB.convertToDictionary(bson: $0)})
						.sorted {Int($0["order"]!)! < Int($1["order"]!)!}
	let nodes = try Node(node: information.flatMap {try? Node(node: $0)})
	return try drop.view.make("index", ["category": "overview", "data": nodes])
}

drop.get("skills") { req in
	guard let cursor = mongoDB.cursor else {
		print("Database cannot be connected")
		throw Abort.badRequest
	}
	let data = cursor["skillContent"]
	let information = Array(try data.find()).map({mongoDB.convertToDictionary(bson: $0)})
						.sorted {Int($0["order"]!)! < Int($1["order"]!)!}
	let nodes = try Node(node: information.flatMap {try? Node(node: $0)})
	return try drop.view.make("index", ["category": "skills",  "data": nodes])
}

drop.get("projects") { req in
	guard let cursor = mongoDB.cursor else {
		print("Database cannot be connected")
		throw Abort.badRequest
	}
	let data = cursor["projectContent"]
	let information = Array(try data.find()).map({mongoDB.convertToDictionary(bson: $0)})
						.sorted {Int($0["order"]!)! < Int($1["order"]!)!}
	let nodes = try Node(node: information.flatMap {try? Node(node: $0)})
	return try drop.view.make("index", ["category": "projects", "data": nodes])
}

drop.get("experience") { req in
	guard let cursor = mongoDB.cursor else {
		print("Database cannot be connected")
		throw Abort.badRequest
	}
	let data = cursor["experienceContent"]
	let information = Array(try data.find()).map({mongoDB.convertToDictionary(bson: $0)})
						.sorted {Int($0["order"]!)! > Int($1["order"]!)!}
	let nodes = try Node(node: information.flatMap {try? Node(node: $0)})
	return try drop.view.make("index", ["category": "experience", "data": nodes])
}

drop.get("contact") { req in
	guard let cursor = mongoDB.cursor else {
		print("Database cannot be connected")
		throw Abort.badRequest
	}
	let data = cursor["contactContent"]
	let information = Array(try data.find()).map({mongoDB.convertToDictionary(bson: $0)})
						.sorted {Int($0["order"]!)! < Int($1["order"]!)!}
	let nodes = try Node(node: information.flatMap {try? Node(node: $0)})
	return try drop.view.make("index", ["category": "contact", "data": nodes])
}

drop.get("overview") { req in
	guard let cursor = mongoDB.cursor else {
		print("Database cannot be connected")
		throw Abort.badRequest
	}
	let data = cursor["overviewContent"]
	let information = Array(try data.find()).map({mongoDB.convertToDictionary(bson: $0)})
						.sorted {Int($0["order"]!)! < Int($1["order"]!)!}
	let nodes = try Node(node: information.flatMap {try? Node(node: $0)})
	return try drop.view.make("index", ["category": "overview", "data": nodes])
}
drop.run()
