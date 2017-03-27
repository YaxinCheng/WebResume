import Vapor
import MongoKitten
import Foundation

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

drop.post("ipconfig") { req in 
	guard 
		let category = req.data["category"]?.string,
		let org = req.data["org"]?.string,
		let postal = req.data["postal"]?.string,
		let country = req.data["country"]?.string,
		let ip = req.data["ip"]?.string,
		let city = req.data["city"]?.string,
		let region = req.data["region"]?.string,
		let loc = req.data["loc"]?.string
	else { return "Not enough information" }
	guard let cursor = mongoDB.cursor else {
		print("Database cannot be connected")
		throw Abort.badRequest
	}
	let date = Date()
	let dateFmt = DateFormatter()
	dateFmt.dateFormat = "yyyy-MM-dd hh:mm:ss"
	dateFmt.timeZone = TimeZone(identifier: "America/Halifax")
	let dateStr = dateFmt.string(from: date)

	let collection = cursor[category + "Visitor"]
	var mainData: Document = ["org": org, "postal": postal, "country": country, "region": region, "city": city, "loc": loc, "time": dateStr]
	if try collection.count(matching: ["_id": ip]) > 0 {
		try collection.update(matching: ["_id": ip], to: mainData)
	} else {
		mainData["_id"] = ip
		try collection.insert(mainData)
	}
	return "success"
}
drop.run()
