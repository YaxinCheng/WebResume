import Vapor
import MongoKitten
import Foundation

let drop = Droplet()
let mongoDB = MongoDB()

func convertToNode(bson: Document) throws -> Node {
	var result = [String: Node]()
	var arrayResult = [Node]()
	for (key, value) in bson {
		if value is Document {
			if let _ = Int(key) {
				arrayResult.append(try convertToNode(bson: value as! Document))
			} else {
				result[key] = try convertToNode(bson: value as! Document)
			}
		} else {
			if let _ = Int(key) {
				arrayResult.append(try Node(node: value is String ? value as! String : "\(value)"))
			} else {
				result[key] = try Node(node: value is String ? value as! String : "\(value)")
			}
		}
	}
	return arrayResult.isEmpty ? try Node(node: result) : try Node(node: arrayResult)
}

func queryData(cursor: String, sortAscend: Bool = true) throws -> Node {
	guard let mongoCursor = mongoDB.cursor else {
		print("Database cannot be connected")
		throw Abort.badRequest
	}
	let data = mongoCursor[cursor]
	let information = Array(try data.find())
		.sorted { sortAscend ? (Int($0["order"]!)! < Int($1["order"]!)!) : (Int($0["order"]!)! > Int($1["order"]!)!) }
		.flatMap({try? convertToNode(bson: $0)})
	return try Node(node: information)
}

drop.get { req in
	let nodes = try queryData(cursor: "overviewContent")
	return try drop.view.make("index", ["category": "overview", "data": nodes])
}

drop.get("skills") { req in
	let nodes = try queryData(cursor: "skillContent")
	print(nodes)
	return try drop.view.make("index", ["category": "skills",  "data": nodes])
}

drop.get("projects") { req in
	let nodes = try queryData(cursor: "projectContent")
	return try drop.view.make("index", ["category": "projects", "data": nodes])
}

drop.get("experience") { req in
	let nodes = try queryData(cursor: "experienceContent", sortAscend: false)
	return try drop.view.make("index", ["category": "experience", "data": nodes])
}

drop.get("contact") { req in
	let nodes = try queryData(cursor: "contactContent", sortAscend: false)
	return try drop.view.make("index", ["category": "contact", "data": nodes])
}

drop.get("overview") { req in
	let nodes = try queryData(cursor: "overviewContent")
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
