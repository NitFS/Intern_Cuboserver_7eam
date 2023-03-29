using UnityEngine;
using System.Collections;

public class hodilkiesaintist : MonoBehaviour {
	public float speed = 4f;
	float direction = -1f;

	

	void Update () {
		GetComponent<Rigidbody2D>().velocity = new Vector2 ( speed * direction, GetComponent<Rigidbody2D>().velocity.y);
		transform.localScale = new Vector3 (direction, 1, 1);
	}
    void OnCollisionEnter2D(Collision2D col){
		if (col.gameObject.tag == "Wall")
						direction *= -1f;
	}
}
